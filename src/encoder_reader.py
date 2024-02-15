"Authors: Connor Schott, Fermin Moreno, Berent Baysal"

from pyb import Timer, Pin

class Encoder:
    """!
    This class implements an encoder reader.
    """

    def __init__(self, timer, enc_pin_A, enc_pin_B):
        """!
        Creates an encoder reader by configuring encoder pins and timer for encoder counting mode.
        @param timer: Timer for encoder counting
        @param enc_pin_A: Encoder channel A pin
        @param enc_pin_B: Encoder channel B pin
        """
        self.timer = Timer(timer, prescaler=0, period=0xFFFF)
        self.enc_chA = self.timer.channel(1, Timer.ENC_AB, pin=enc_pin_A)
        self.enc_chB = self.timer.channel(2, Timer.ENC_AB, pin=enc_pin_B)

        self.encoder_value1 = None  # Initialize encoder value
        self.encoder_value2 = None  # Initialize encoder value
        
        self.prev_chA_value = self.enc_chA.capture()  # Store previous channel A value
        self.prev_chB_value = self.enc_chB.capture()  # Store previous channel B value
        
        print("Creating an encoder reader")

    def zero(self):
        """
        Sets the count to zero at the current position for both encoders.
        """
        if self.encoder_value1 is None:
            self.encoder_value1 = 0
        
        if self.encoder_value2 is None:
            self.encoder_value2 = 0

    def read(self):
        """!
        This method reads the encoder values.
        @return: Tuple containing the current encoder count, delta, and channel A and B values
        """
        # Capture current channel A and B values
        curr_chA_value = self.enc_chA.capture()
        curr_chB_value = self.enc_chB.capture()

        # Calculate delta based on channel A value change
        delta1 = curr_chA_value - self.prev_chA_value
        delta2 = curr_chB_value - self.prev_chB_value

        # Handle overflow and underflow conditions
        if delta1 > 32767:
            delta1 -= 65536
        elif delta1 < -32768:
            delta1 += 65536

        # Update encoder value
        if self.encoder_value1 is None:
            self.encoder_value1 = delta1
        else:
            self.encoder_value1 += delta1
        
        if delta2 > 32767:
            delta2 -= 65536
        elif delta2 < -32768:
            delta2 += 65536
        
        if self.encoder_value2 is None:
            self.encoder_value2 = delta2
        else:
            self.encoder_value2 += delta2

        # Store current values for next iteration
        self.prev_chA_value = curr_chA_value
        self.prev_chB_value = curr_chB_value

        return self.encoder_value1, self.encoder_value2

if __name__ == '__main__':
    # Specify encoder pins and timers for encoder1 and encoder2
    encoder1 = Encoder(4, Pin.board.PB6, Pin.board.PB7)
    encoder2 = Encoder(8, Pin.board.PC6, Pin.board.PC7)
    
    while True:
        # Read encoder1 values
        encoder1_value = encoder1.read()
        
        # Read encoder2 values
        encoder2_value = encoder2.read()

        # Print out values for both encoders
        
        print("Encoder 1 Value:", encoder1_value)
        print()
        print("Encoder 2 Value:", encoder2_value)
        print()
        pyb.delay(50)  # Adjust delay for higher precision
