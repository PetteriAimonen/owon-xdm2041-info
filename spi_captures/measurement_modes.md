DC voltage 5 V
==============

    Relays = 0x11
    R20 = C2   SCMPI = 6, ENCMP = 0, ENCTR = 0
    R21 = 21   SCMPRH = 2, SCMPRL = 1
    R22 = 14   AD1OS = 0, AD1CHOP = 2, AD1OSR = 4
    R23 = 8B   ENAD1 = 1, AD1RG = 0, AD1RHBUF = 1, AD1RLBUF = 0, AD1IPBUF=1, AD1INBUF=1
    R24 = 85   SAD1FP = 8, SDIO = 0, SAD1FN = 5
    R25 = 11   AD1IG = 1
    R26 = 08   ADC2 not used
    R27 = 15   SAD2IP = 0, SAD2IN = 1, SAD2RH = 1, SAD2RL = 1
    R28 = 31   SAD1RH = 3, SAD1RL = 1
    R29 = F8
    R2A = 00   PA1 = 0, PA0 = 0
    R2B = 00   PA3 = 0, PA2 = 0
    R2C = 00   PA5 = 0, PA4 = 0
    R2D = 00   PA7 = 0, PA6 = 0
    R2E = 08   PA9 = 0, PA8 = PS
    R2F = 81   ENVS = 1, SMODE = 1
    R30 = 80   SREFO = 1, ACC = 0
    R31 = C7   ENREFO = 1, ENBIAS = 1, SAGND = 0, SFUVR = 7
    R32 = 33   ENOP2 = 0, SOP2P = 3, ENOP1 = 0, SOP1P = 3
    R33 = A8   OP1CHOP = 2, ENOSC = 1, ENXI = 0, SFT1 = 2, SAD1I = 0
    R34 = 00   ADC3 not used
    R35 = 00   ADC3 not used
    R36 = 00
    R37 = 00

Measurement is based on ADC1.

Input gain is set by AD1IG = 1, giving 1.8x input gain.
Reference rail gain is set by AD1RG = 0, giving 1x ref gain.
Positive and negative buffers are enabled with AD1IPBUF and AD1INBUF.

Oversample rate is set to 4096x by AD1OSR = 4.

ADC1 input is selected by SAD1I = 0, which is the prefilter AD1FP/AD1FN.
Prefilter is configured by SFT1 = 2, which connects the external C7 but without extra series resistors.

Prefilter input is set by SAD1FP = 8 and SAD1FN = 5, giving positive input PB0 and negative input PB3.
PB0 is fed through U19 switch from V/R input terminal, with 560 kohm series resistance.
PB3 is connected to AGND with 1 kohm series resistor.

Reference rails are selected by SAD1RH = 3 and SAD1RL = 1, which give PB6 as REFH and AGND as REFL.
PB6 is external 1.25 volt reference.

Seems straightforward otherwise, but it seems this should give a measurement range of 0..1.25V or perhaps +-1.25V, not +-5V.
So where is the missing 5x divider?




