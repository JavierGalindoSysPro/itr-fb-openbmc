#!/usr/bin/env python3
#
# Copyright 2019-present Facebook. All Rights Reserved.
#
# This program file is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation; version 2 of the License.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
# for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program in a file named COPYING; if not, write to the
# Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA
#

GPIOS = {
    "BMC_BIOS_FLASH_CTRL": {
        "active_low": "0",
        "direction": "in",
        "edge": "none",
        "uevent": "",
        "value": "0",
    },
    "BMC_CPLD_FPGA_SEL": {
        "active_low": "0",
        "direction": "out",
        "edge": "none",
        "uevent": "",
        "value": "1",
    },
    "BMC_DEBUG_EN_N": {
        "active_low": "0",
        "direction": "in",
        "edge": "none",
        "uevent": "",
        "value": "1",
    },
    "BMC_FAULT_N": {
        "active_low": "0",
        "direction": "out",
        "edge": "none",
        "uevent": "",
        "value": "1",
    },
    "BMC_JTAG_SEL": {
        "active_low": "0",
        "direction": "out",
        "edge": "none",
        "uevent": "",
        "value": "1",
    },
    "BMC_PPIN": {
        "active_low": "0",
        "direction": "out",
        "edge": "none",
        "uevent": "",
        "value": "1",
    },
    "BMC_PRDY_N": {
        "active_low": "0",
        "direction": "in",
        "edge": "none",
        "uevent": "",
        "value": "1",
    },
    "BMC_PREQ_N": {
        "active_low": "0",
        "direction": "out",
        "edge": "none",
        "uevent": "",
        "value": "1",
    },
    "BMC_PWR_DEBUG_N": {
        "active_low": "0",
        "direction": "in",
        "edge": "none",
        "uevent": "",
        "value": "0",
    },
    "BMC_READY_N": {
        "active_low": "0",
        "direction": "out",
        "edge": "none",
        "uevent": "",
        "value": "0",
    },
    "BMC_TCK_MUX_SEL": {
        "active_low": "0",
        "direction": "in",
        "edge": "none",
        "uevent": "",
        "value": "0",
    },
    "BMC_XDP_PRSNT_IN_N": {
        "active_low": "0",
        "direction": "in",
        "edge": "none",
        "uevent": "",
        "value": "1",
    },
    "FM_BATTERY_SENSE_EN_N": {
        "active_low": "0",
        "direction": "out",
        "edge": "none",
        "uevent": "",
        "value": "1",
    },
    "FM_BIOS_MRC_DEBUG_MSG_DIS_N": {
        "active_low": "0",
        "direction": "out",
        "edge": "none",
        "uevent": "",
        "value": "1",
    },
    "FM_BIOS_POST_CMPLT_N": {
        "active_low": "0",
        "direction": "in",
        "edge": "none",
        "uevent": "",
        "value": "0",
    },
    "FM_BIOS_SMI_ACTIVE_N": {
        "active_low": "0",
        "direction": "in",
        "edge": "none",
        "uevent": "",
        "value": "1",
    },
    "FM_BMC_PWRBTN_OUT_N": {
        "active_low": "0",
        "direction": "out",
        "edge": "none",
        "uevent": "",
        "value": "1",
    },
    "FM_BOARD_REV_ID0": {
        "active_low": "0",
        "direction": "in",
        "edge": "none",
        "uevent": "",
        "value": "1",
    },
    "FM_BOARD_REV_ID1": {
        "active_low": "0",
        "direction": "in",
        "edge": "none",
        "uevent": "",
        "value": "0",
    },
    "FM_BOARD_REV_ID2": {
        "active_low": "0",
        "direction": "in",
        "edge": "none",
        "uevent": "",
        "value": "1",
    },
    "FM_BOARD_SKU_ID0": {
        "active_low": "0",
        "direction": "in",
        "edge": "none",
        "uevent": "",
        "value": "1",
    },
    "FM_BOARD_SKU_ID1": {
        "active_low": "0",
        "direction": "in",
        "edge": "none",
        "uevent": "",
        "value": "1",
    },
    "FM_BOARD_SKU_ID2": {
        "active_low": "0",
        "direction": "in",
        "edge": "none",
        "uevent": "",
        "value": "0",
    },
    "FM_BOARD_SKU_ID3": {
        "active_low": "0",
        "direction": "in",
        "edge": "none",
        "uevent": "",
        "value": "1",
    },
    "FM_BOARD_SKU_ID4": {
        "active_low": "0",
        "direction": "in",
        "edge": "none",
        "uevent": "",
        "value": "0",
    },
    "FM_BOARD_SKU_ID5": {
        "active_low": "0",
        "direction": "in",
        "edge": "none",
        "uevent": "",
        "value": "0",
    },
    "FM_BOARD_SKU_ID6": {
        "active_low": "0",
        "direction": "in",
        "edge": "none",
        "uevent": "",
        "value": "0",
    },
    "FM_CPU0_FIVR_FAULT_LVT3_N": {
        "active_low": "0",
        "direction": "in",
        "edge": "both",
        "uevent": "",
        "value": "1",
    },
    "FM_CPU0_PROCHOT_LVT3_BMC_N": {
        "active_low": "0",
        "direction": "in",
        "edge": "both",
        "uevent": "",
        "value": "1",
    },
    "FM_CPU0_RC_ERROR_N": {
        "active_low": "0",
        "direction": "in",
        "edge": "both",
        "uevent": "",
        "value": "1",
    },
    "FM_CPU0_SKTOCC_LVT3_N": {
        "active_low": "0",
        "direction": "in",
        "edge": "both",
        "uevent": "",
        "value": "0",
    },
    "FM_CPU0_THERMTRIP_LATCH_LVT3_N": {
        "active_low": "0",
        "direction": "in",
        "edge": "both",
        "uevent": "",
        "value": "1",
    },
    "FM_CPU1_FIVR_FAULT_LVT3_N": {
        "active_low": "0",
        "direction": "in",
        "edge": "both",
        "uevent": "",
        "value": "1",
    },
    "FM_CPU1_PROCHOT_LVT3_BMC_N": {
        "active_low": "0",
        "direction": "in",
        "edge": "both",
        "uevent": "",
        "value": "1",
    },
    "FM_CPU1_RC_ERROR_N": {
        "active_low": "0",
        "direction": "in",
        "edge": "both",
        "uevent": "",
        "value": "1",
    },
    "FM_CPU1_SKTOCC_LVT3_N": {
        "active_low": "0",
        "direction": "in",
        "edge": "both",
        "uevent": "",
        "value": "0",
    },
    "FM_CPU1_THERMTRIP_LATCH_LVT3_N": {
        "active_low": "0",
        "direction": "in",
        "edge": "both",
        "uevent": "",
        "value": "1",
    },
    "FM_CPU_CATERR_LVT3_N": {
        "active_low": "0",
        "direction": "in",
        "edge": "falling",
        "uevent": "",
        "value": "1",
    },
    "FM_CPU_ERR0_LVT3_BMC_N": {
        "active_low": "0",
        "direction": "in",
        "edge": "both",
        "uevent": "",
        "value": "1",
    },
    "FM_CPU_ERR1_LVT3_BMC_N": {
        "active_low": "0",
        "direction": "in",
        "edge": "both",
        "uevent": "",
        "value": "1",
    },
    "FM_CPU_ERR2_LVT3_N": {
        "active_low": "0",
        "direction": "in",
        "edge": "both",
        "uevent": "",
        "value": "1",
    },
    "FM_CPU_MSMI_LVT3_N": {
        "active_low": "0",
        "direction": "in",
        "edge": "falling",
        "uevent": "",
        "value": "1",
    },
    "FM_FAST_PROCHOT_EN_N": {
        "active_low": "0",
        "direction": "out",
        "edge": "none",
        "uevent": "",
        "value": "0",
    },
    "FM_FORCE_ADR_N": {
        "active_low": "0",
        "direction": "out",
        "edge": "none",
        "uevent": "",
        "value": "1",
    },
    "FM_GLOBAL_RST_WARN_N": {
        "active_low": "0",
        "direction": "in",
        "edge": "none",
        "uevent": "",
        "value": "1",
    },
    "FM_HSC_TIMER_EXP_N": {
        "active_low": "0",
        "direction": "in",
        "edge": "both",
        "uevent": "",
        "value": "1",
    },
    "FM_MEM_THERM_EVENT_PCH_N": {
        "active_low": "0",
        "direction": "in",
        "edge": "both",
        "uevent": "",
        "value": "1",
    },
    "FM_OCP_MEZZA_PRES": {
        "active_low": "0",
        "direction": "in",
        "edge": "none",
        "uevent": "",
        "value": "1",
    },
    "FM_OC_DETECT_EN_N": {
        "active_low": "0",
        "direction": "out",
        "edge": "none",
        "uevent": "",
        "value": "0",
    },
    "FM_PCH_BMC_THERMTRIP_N": {
        "active_low": "0",
        "direction": "in",
        "edge": "both",
        "uevent": "",
        "value": "1",
    },
    "FM_PMBUS_ALERT_BUF_EN_N": {
        "active_low": "0",
        "direction": "out",
        "edge": "none",
        "uevent": "",
        "value": "0",
    },
    "FM_POST_CARD_PRES_BMC_N": {
        "active_low": "0",
        "direction": "in",
        "edge": "both",
        "uevent": "",
        "value": "1",
    },
    "FM_PWR_BTN_N": {
        "active_low": "0",
        "direction": "in",
        "edge": "both",
        "uevent": "",
        "value": "1",
    },
    "FM_SLPS4_N": {
        "active_low": "0",
        "direction": "in",
        "edge": "falling",
        "uevent": "",
        "value": "1",
    },
    "FM_THROTTLE_N": {
        "active_low": "0",
        "direction": "in",
        "edge": "both",
        "uevent": "",
        "value": "1",
    },
    "FM_UARTSW_LSB_N": {
        "active_low": "0",
        "direction": "in",
        "edge": "both",
        "uevent": "",
        "value": "0",
    },
    "FM_UARTSW_MSB_N": {
        "active_low": "0",
        "direction": "in",
        "edge": "both",
        "uevent": "",
        "value": "1",
    },
    "FM_UV_ADR_TRIGGER_EN": {
        "active_low": "0",
        "direction": "out",
        "edge": "none",
        "uevent": "",
        "value": "1",
    },
    "FP_NMI_BTN_N": {
        "active_low": "0",
        "direction": "in",
        "edge": "both",
        "uevent": "",
        "value": "1",
    },
    "HSC_SMBUS_SWITCH_EN": {
        "active_low": "0",
        "direction": "in",
        "edge": "none",
        "uevent": "",
        "value": "1",
    },
    "H_CPU0_MEMABC_MEMHOT_LVT3_BMC_N": {
        "active_low": "0",
        "direction": "in",
        "edge": "both",
        "uevent": "",
        "value": "1",
    },
    "H_CPU0_MEMDEF_MEMHOT_LVT3_BMC_N": {
        "active_low": "0",
        "direction": "in",
        "edge": "both",
        "uevent": "",
        "value": "1",
    },
    "H_CPU1_MEMGHJ_MEMHOT_LVT3_BMC_N": {
        "active_low": "0",
        "direction": "in",
        "edge": "both",
        "uevent": "",
        "value": "1",
    },
    "H_CPU1_MEMKLM_MEMHOT_LVT3_BMC_N": {
        "active_low": "0",
        "direction": "in",
        "edge": "both",
        "uevent": "",
        "value": "1",
    },
    "IRQ_DIMM_SAVE_LVT3_N": {
        "active_low": "0",
        "direction": "in",
        "edge": "both",
        "uevent": "",
        "value": "1",
    },
    "IRQ_HSC_FAULT_N": {
        "active_low": "0",
        "direction": "in",
        "edge": "both",
        "uevent": "",
        "value": "1",
    },
    "IRQ_OC_DETECT_N": {
        "active_low": "0",
        "direction": "in",
        "edge": "both",
        "uevent": "",
        "value": "1",
    },
    "IRQ_PVCCIN_CPU0_VRHOT_LVC3_N": {
        "active_low": "0",
        "direction": "in",
        "edge": "both",
        "uevent": "",
        "value": "1",
    },
    "IRQ_PVCCIN_CPU1_VRHOT_LVC3_N": {
        "active_low": "0",
        "direction": "in",
        "edge": "both",
        "uevent": "",
        "value": "1",
    },
    "IRQ_PVDDQ_ABC_VRHOT_LVT3_N": {
        "active_low": "0",
        "direction": "in",
        "edge": "both",
        "uevent": "",
        "value": "1",
    },
    "IRQ_PVDDQ_DEF_VRHOT_LVT3_N": {
        "active_low": "0",
        "direction": "in",
        "edge": "both",
        "uevent": "",
        "value": "1",
    },
    "IRQ_PVDDQ_GHJ_VRHOT_LVT3_N": {
        "active_low": "0",
        "direction": "in",
        "edge": "both",
        "uevent": "",
        "value": "1",
    },
    "IRQ_PVDDQ_KLM_VRHOT_LVT3_N": {
        "active_low": "0",
        "direction": "in",
        "edge": "both",
        "uevent": "",
        "value": "1",
    },
    "IRQ_SML1_PMBUS_ALERT_N": {
        "active_low": "0",
        "direction": "in",
        "edge": "both",
        "uevent": "",
        "value": "1",
    },
    "IRQ_UV_DETECT_N": {
        "active_low": "0",
        "direction": "in",
        "edge": "both",
        "uevent": "",
        "value": "1",
    },
    "LED_POST_CODE_0": {
        "active_low": "0",
        "direction": "out",
        "edge": "none",
        "uevent": "",
        "value": "1",
    },
    "LED_POST_CODE_1": {
        "active_low": "0",
        "direction": "out",
        "edge": "none",
        "uevent": "",
        "value": "0",
    },
    "LED_POST_CODE_2": {
        "active_low": "0",
        "direction": "out",
        "edge": "none",
        "uevent": "",
        "value": "1",
    },
    "LED_POST_CODE_3": {
        "active_low": "0",
        "direction": "out",
        "edge": "none",
        "uevent": "",
        "value": "1",
    },
    "LED_POST_CODE_4": {
        "active_low": "0",
        "direction": "out",
        "edge": "none",
        "uevent": "",
        "value": "0",
    },
    "LED_POST_CODE_5": {
        "active_low": "0",
        "direction": "out",
        "edge": "none",
        "uevent": "",
        "value": "1",
    },
    "LED_POST_CODE_6": {
        "active_low": "0",
        "direction": "out",
        "edge": "none",
        "uevent": "",
        "value": "0",
    },
    "LED_POST_CODE_7": {
        "active_low": "0",
        "direction": "out",
        "edge": "none",
        "uevent": "",
        "value": "1",
    },
    "PECI_MUX_SELECT": {
        "active_low": "0",
        "direction": "in",
        "edge": "none",
        "uevent": "",
        "value": "0",
    },
    "PWRGD_SYS_PWROK": {
        "active_low": "0",
        "direction": "in",
        "edge": "both",
        "uevent": "",
        "value": "1",
    },
    "RST_BMC_PLTRST_BUF_N": {
        "active_low": "0",
        "direction": "in",
        "edge": "both",
        "uevent": "",
        "value": "1",
    },
    "RST_BMC_SYSRST_BTN_OUT_N": {
        "active_low": "0",
        "direction": "out",
        "edge": "none",
        "uevent": "",
        "value": "1",
    },
    "RST_RSMRST_N": {
        "active_low": "0",
        "direction": "in",
        "edge": "none",
        "uevent": "",
        "value": "1",
    },
    "RST_SYSTEM_BTN_N": {
        "active_low": "0",
        "direction": "in",
        "edge": "both",
        "uevent": "",
        "value": "1",
    },
    "SERVER_POWER_LED": {
        "active_low": "0",
        "direction": "out",
        "edge": "none",
        "uevent": "",
        "value": "1",
    },
    "UV_HIGH_SET": {
        "active_low": "0",
        "direction": "in",
        "edge": "none",
        "uevent": "",
        "value": "1",
    },
}
