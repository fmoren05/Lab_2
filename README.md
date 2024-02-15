# Lab_2
# Encoder Reader
# This Python program is designed to read encoder values from two encoders connected to an STM32 microcontroller.
# It implements an `Encoder` class that encapsulates the functionality required for reading encoder values.



## Setup and Usage

### Encoders
# The program assumes the use of incremental encoders, commonly used to measure the motion of devices.
# These encoders send digital signals over two wires in Gray Code, also known as quadrature signals.

### Encoder Reading Procedure
# 1. Connect the encoder power and ground leads to the GND and 3V3 leads on the Shoe Board's screw terminals.
# 2. Connect encoder channels A and B to pins B6 and B7 of the Shoe Board's screw terminal block.
# 3. Connect USB to the Shoe to power the system.
# 4. Write code that sets up a timer and its CH1 and CH2 channels in encoder counting mode.
# 5. Test the code by rotating the motor attached to the encoder by hand and verifying the readings.



### Basic Functions

# `__init__()` Constructor method initializes the `Encoder` object by configuring encoder pins
# and a timer for encoder counting mode.
# `read()` Method retrieves the current position of the encoder.
# It returns a tuple containing the current encoder count, delta, and channel A and B values.
# `zero()` Method sets the count to zero at the current position for both encoders.

### Encoder Reader Class
# The `Encoder` class provided in the code encapsulates the operation of the timer to read encoders.
# It offers the basic methods mentioned above along with additional functionalities if needed.

### Testing
# Test the encoder class by manually rotating the motor and running the motor under power.
# Ensure that the readings are reasonable and accurate, even when the motor is moving quickly.

## Overflow Handling
# The program addresses potential timer overflow and underflow issues.
# It ensures that the total position moved is correctly calculated even in cases of overflow or underflow.



## Files
# - `encoder_reader.py`: Contains the `Encoder` class and main code for reading encoder values.
# - `README.md`: This file, providing an overview of the program, usage instructions, and basic functions. 
