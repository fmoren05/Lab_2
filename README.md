# Lab_2

Authors: Conor Schott, Fermin Moreno, Berent Baysal
Class: Encoder
Date: 15th February 2024
Description:
    This script implements an encoder reader using Pyboard's Timer and Pin modules.
    It provides a class called Encoder that allows reading encoder values from two different encoders.

Usage:
    1. Ensure Pyboard is connected.
    2. Specify encoder pins and timers for encoder1 and encoder2.
    3. Run the script. It will continuously read encoder values and print them.

Encoder Class:
    - __init__(timer, enc_pin_A, enc_pin_B): Constructor method for the Encoder class.
    - read(): Method to read the encoder values.
    - zero(): Method to reset the encoder count to zero.

Dependencies:
    - pyb: This script requires the Pyboard module pyb.

Note:
    - Ensure the specified pins and timers are correctly connected to the encoders.
    - Adjust the script as needed for specific encoder setups and behaviors.
