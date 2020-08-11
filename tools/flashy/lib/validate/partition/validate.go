/**
 * Copyright 2020-present Facebook. All Rights Reserved.
 *
 * This program file is free software; you can redistribute it and/or modify it
 * under the terms of the GNU General Public License as published by the
 * Free Software Foundation; version 2 of the License.
 *
 * This program is distributed in the hope that it will be useful, but WITHOUT
 * ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
 * FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
 * for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program in a file named COPYING; if not, write to the
 * Free Software Foundation, Inc.,
 * 51 Franklin Street, Fifth Floor,
 * Boston, MA 02110-1301 USA
 */

package partition

import (
	"log"

	"github.com/pkg/errors"
)

// get all the partitions based on the partitionConfigs
// then validate them. If all passed, return nil. Else return the error.
var ValidatePartitionsFromPartitionConfigs = func(
	data []byte,
	partitionConfigs []PartitionConfigInfo,
) error {
	partitions, err := getAllPartitionsFromPartitionConfigs(
		data,
		partitionConfigs,
	)
	if err != nil {
		return errors.Errorf("Unable to get all partitions: %v",
			err)
	}
	err = validatePartitions(partitions)
	if err != nil {
		return errors.Errorf("Validation failed: %v", err)
	}
	return nil
}

// calls validate for all partitions, and returns an error if a partition
// failed validation. If all partitions pass validation, return nil
var validatePartitions = func(partitions []Partition) error {
	for _, p := range partitions {
		log.Printf("Validating partition '%v' using '%v' partition validator",
			p.GetName(), p.GetType())
		err := p.Validate()
		if err != nil {
			return errors.Errorf("Partition '%v' failed validation: %v",
				p.GetName(), err)
		}
	}
	return nil
}

// Try to get all partitions based on partition configs.
// Return an error if unknown partition config type or failed to get.
var getAllPartitionsFromPartitionConfigs = func(
	data []byte,
	partitionConfigs []PartitionConfigInfo,
) ([]Partition, error) {
	partitions := []Partition{}

	for _, pInfo := range partitionConfigs {
		// Image format may contain mtd-only partitions (such as data partitions).
		// These are not included in image files, and these partitions' validations are ignored anyway.
		// TOOD:- for flash device: verify JFFS2 filesystem integrity
		if pInfo.Offset >= uint32(len(data)) {
			if pInfo.Type == IGNORE { // make sure it's IGNORE, otherwise fail it
				log.Printf("Ignoring validation of '%v' partition: given offset %vB larger than "+
					"size of data %vB", pInfo.Name, pInfo.Offset, uint32(len(data)))
				continue
			} else {
				return nil, errors.Errorf("Wanted start offset (%v) of '%v' partition larger "+
					"than data size (%v)",
					pInfo.Offset, pInfo.Name, uint32(len(data)))
			}
		}

		// flash size is 32MB, so pInfo may indicate a size
		// larger than the image file. (this is fine with flash devices are they are 32MB)
		// In such a case, reduce the size of the partition in pInfo.
		// The alternative would be to pad the image with zero bytes until 32MB,
		// but that would require operating on a new copy of the image in memory.
		// Golang mmap unfortunately doesn't expose the addr argument to allow
		// fixed mapping (we could map a 23MB image file over a 32MB /dev/zero file)
		pOffsetEnd := pInfo.Size + pInfo.Offset
		if uint32(len(data)) < pOffsetEnd {
			actualPartitionSize := uint32(len(data)) - pInfo.Offset
			pInfo.Size = actualPartitionSize
			pOffsetEnd = uint32(len(data))
		}

		// only pass in region of data defined as the partition
		pData := data[pInfo.Offset:pOffsetEnd]
		args := PartitionFactoryArgs{
			Data:  pData,
			PInfo: pInfo,
		}

		if factory, ok := PartitionFactoryMap[pInfo.Type]; ok {
			p := factory(args)
			partitions = append(partitions, p)
		} else {
			return nil, errors.Errorf("Failed to get '%v' partition: "+
				" Unknown partition validator type '%v'",
				pInfo.Name, pInfo.Type)
		}
	}
	return partitions, nil
}
