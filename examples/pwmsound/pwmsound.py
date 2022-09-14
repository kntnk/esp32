"""
ampy run test.py
"""
from machine import Pin, PWM
import time

class Note():
    NONE = 1.00000
    C0  = 16.35160
    CS0 = 17.32391
    D0  = 18.35405
    DS0 = 19.44544
    E0  = 20.60172
    F0  = 21.82676
    FS0 = 23.12465
    G0  = 24.49971
    GS0 = 25.95654
    A0  = 27.50000
    AS0 = 29.13524
    B0  = 30.86771
    C1  = 32.70320
    CS1 = 34.64783
    D1  = 36.70810
    DS1 = 38.89087
    E1  = 41.20344
    F1  = 43.65353
    FS1 = 46.24930
    G1  = 48.99943
    GS1 = 51.91309
    A1  = 55.00000
    AS1 = 58.27047
    B1  = 61.73541
    C2  = 65.40639
    CS2 = 69.29566
    D2  = 73.41619
    DS2 = 77.78175
    E2  = 82.40689
    F2  = 87.30706
    FS2 = 92.49861
    G2  = 97.99886
    GS2 = 103.8262
    A2  = 110.0000
    AS2 = 116.5409
    B2  = 123.4708
    C3  = 130.8128
    CS3 = 138.5913
    D3  = 146.8324
    DS3 = 155.5635
    E3  = 164.8138
    F3  = 174.6141
    FS3 = 184.9972
    G3  = 195.9977
    GS3 = 207.6523
    A3  = 220.0000
    AS3 = 233.0819
    B3  = 246.9417
    C4  = 261.6256
    CS4 = 277.1826
    D4  = 293.6648
    DS4 = 311.1270
    E4  = 329.6276
    F4  = 349.2282
    FS4 = 369.9944
    G4  = 391.9954
    GS4 = 415.3047
    A4  = 440.0000
    AS4 = 466.1638
    B4  = 493.8833
    C5  = 523.2511
    CS5 = 554.3653
    D5  = 587.3295
    DS5 = 622.2540
    E5  = 659.2551
    F5  = 698.4565
    FS5 = 739.9888
    G5  = 783.9909
    GS5 = 830.6094
    A5  = 880.0000
    AS5 = 932.3275
    B5  = 987.7666
    C6  = 1046.502
    CS6 = 1108.731
    D6  = 1174.659
    DS6 = 1244.508
    E6  = 1318.510
    F6  = 1396.913
    FS6 = 1479.978
    G6  = 1567.982
    GS6 = 1661.219
    A6  = 1760.000
    AS6 = 1864.655
    B6  = 1975.533
    C7  = 2093.005
    CS7 = 2217.461
    D7  = 2349.318
    DS7 = 2489.016
    E7  = 2637.020
    F7  = 2793.826
    FS7 = 2959.955
    G7  = 3135.963
    GS7 = 3322.438
    A7  = 3520.000
    AS7 = 3729.310
    B7  = 3951.066
    C8  = 4186.009
    CS8 = 4434.922
    D8  = 4698.636
    DS8 = 4978.032
    E8  = 5274.041
    F8  = 5587.652
    FS8 = 5919.911
    G8  = 6271.927
    GS8 = 6644.875
    A8  = 7040.000
    AS8 = 7458.620
    B8  = 7902.133


class Huzzah:
    def __init__(self, pinLED=13):
        self.pinLED = pinLED

    def ledOn(self):
        led = Pin(self.pinLED, Pin.OUT)
        led.value(1)

    def ledOff(self):
        led = Pin(self.pinLED, Pin.OUT)
        led.value(0)

    def blink(self):
        self.ledOn()
        time.sleep(1)
        self.ledOff()
        time.sleep(1)


class Music:
    def __init__(self, pinPWM):
        self.pinPWM = pinPWM
        self.esp = Huzzah()

    def melody_list(self):
        mario = [
        Note.E7,    Note.E7,    Note.NONE,  Note.E7,    Note.NONE,  Note.C7,    Note.E7,    Note.NONE,
        Note.G7,    Note.NONE,  Note.NONE,  Note.NONE,  Note.G6,    Note.NONE,  Note.NONE,  Note.NONE,

        Note.C7,    Note.NONE,  Note.NONE,  Note.G6,    Note.NONE,  Note.NONE,  Note.E6,    Note.NONE,
        Note.NONE,  Note.A6,    Note.NONE,  Note.B6,    Note.NONE,  Note.AS6,   Note.A6,    Note.NONE,
        Note.G6,    Note.E7,    Note.NONE,  Note.G7,    Note.A7,    Note.NONE,  Note.F7,    Note.G7,
        Note.NONE,  Note.E7,    Note.NONE,  Note.C7,    Note.D7,    Note.B6,    Note.NONE,  Note.NONE,

        Note.C7,    Note.NONE,  Note.NONE,  Note.G6,    Note.NONE,  Note.NONE,  Note.E6,    Note.NONE,
        Note.NONE,  Note.A6,    Note.NONE,  Note.B6,    Note.NONE,  Note.AS6,   Note.A6,    Note.NONE,
        Note.G6,    Note.E7,    Note.NONE,  Note.G7,    Note.A7,    Note.NONE,  Note.F7,    Note.G7,
        Note.NONE,  Note.E7,    Note.NONE,  Note.C7,    Note.D7,    Note.B6,    Note.NONE,  Note.NONE,

        Note.NONE,  Note.G7,    Note.FS7,   Note.F7,    Note.D7,    Note.NONE,  Note.E7,    Note.NONE,
        Note.G6,    Note.A6,    Note.C7,    Note.NONE,  Note.A6,    Note.C7,    Note.D7,    Note.NONE,
        Note.NONE,  Note.G7,    Note.FS7,   Note.F7,    Note.D7,    Note.NONE,  Note.E7,    Note.NONE,
        Note.C8,    Note.NONE,  Note.C8,    Note.C8,    Note.NONE,  Note.NONE,  Note.NONE,  Note.NONE,

        Note.NONE,  Note.G7,    Note.FS7,   Note.F7,    Note.D7,    Note.NONE,  Note.E7,    Note.NONE,
        Note.G6,    Note.A6,    Note.C7,    Note.NONE,  Note.A6,    Note.C7,    Note.D7,    Note.NONE,
        Note.NONE,  Note.DS7,   Note.NONE,  Note.NONE,  Note.D7,    Note.NONE,  Note.NONE,  Note.C7,
        Note.NONE,  Note.NONE,  Note.NONE,  Note.NONE,  Note.NONE,  Note.NONE,  Note.NONE,  Note.NONE,

        Note.C7,    Note.C7,    Note.NONE,  Note.C7,    Note.NONE,  Note.C7,    Note.D7,    Note.NONE,
        Note.E7,    Note.C7,    Note.NONE,  Note.A6,    Note.G6,    Note.NONE,  Note.NONE,  Note.NONE,
        Note.C7,    Note.C7,    Note.NONE,  Note.C7,    Note.NONE,  Note.C7,    Note.D7,    Note.E7,
        Note.NONE,  Note.NONE,  Note.NONE,  Note.NONE,  Note.NONE,  Note.NONE,  Note.NONE,  Note.NONE,

        Note.C7,    Note.C7,    Note.NONE,  Note.C7,    Note.NONE,  Note.C7,    Note.D7,    Note.NONE,
        Note.E7,    Note.C7,    Note.NONE,  Note.A6,    Note.G6,    Note.NONE,  Note.NONE,  Note.NONE,
        Note.E7,    Note.E7,    Note.NONE,  Note.E7,    Note.NONE,  Note.C7,    Note.E7,    Note.NONE,
        Note.G7,    Note.NONE,  Note.NONE,  Note.NONE,  Note.G6,    Note.NONE,  Note.NONE,  Note.NONE,
        ]
        return mario

    def playPWM(self, melodies, delays=0.15, duty=50):
        pwm = PWM(Pin(self.pinPWM, Pin.OUT))
        for note in melodies:
            print(note)
            if note > 1:
                self.esp.ledOn()
            else:
                self.esp.ledOff()
            pwm.freq(int(note))
            pwm.duty(duty)
            time.sleep(delays)
        pwm.duty(0)
        pwm.deinit()


if __name__ == '__main__':
    pinPWM = 33
    music = Music(pinPWM)
    melodies = music.melody_list()
    music.playPWM(melodies)
