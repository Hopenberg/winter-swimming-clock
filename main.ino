/* Define pin numbers for LEDs, buttons and speaker: */
const uint8_t buttonPins[] = {0, 1, 2, 3};

// https://wokwi.com/projects/383196578309148673

// These are connected to 74HC595 shift register (used to show game score):
const int LATCH_PIN = 18;  // 74HC595 pin 12
const int DATA_PIN = 19;   // 74HC595 pin 14
const int CLOCK_PIN = 9;  // 74HC595 pin 11

byte indexButtonStartDown = 0;
byte indexButtonStartUp = 1;
byte indexButtonAddTime = 2;
byte indexButtonReduceTime = 5;

int counterTime = 0;

byte chosenIndex = 7;


/**
   Set up the Arduino board and initialize Serial communication
*/
void setup() {
  Serial.begin(9600);
  for (byte i = 0; i < 4; i++) {
    pinMode(buttonPins[i], INPUT_PULLUP);
  }
  pinMode(LATCH_PIN, OUTPUT);
  pinMode(CLOCK_PIN, OUTPUT);
  pinMode(DATA_PIN, OUTPUT);
}

/* Digit table for the 7-segment display */
const uint8_t digitTable[] = {
  0b11000000,
  0b11111001,
  0b10100100,
  0b10110000,
  0b10011001,
  0b10010010,
  0b10000010,
  0b11111000,
  0b10000000,
  0b10010000,
};
const uint8_t DASH = 0b10111111;

void sendScore(uint8_t high, uint8_t low) {
  digitalWrite(LATCH_PIN, LOW);
  shiftOut(DATA_PIN, CLOCK_PIN, MSBFIRST, low);
  shiftOut(DATA_PIN, CLOCK_PIN, MSBFIRST, high);
  digitalWrite(LATCH_PIN, HIGH);
}

void displayScore(int seconds) {
  int high = seconds / 10;
  int low = seconds % 10;
  sendScore(high ? digitTable[high] : 0xff, digitTable[low]);
}

/**
    Waits until the user pressed one of the buttons,
    and returns the index of that button
*/
byte readButtons() {
  while (true) {
    for (byte i = 0; i < 4; i++) {
      byte buttonPin = buttonPins[i];
      if (digitalRead(buttonPin) == LOW) {
        return i;
      }
    }
    delay(1);
  }
}

/**
   The main game loop
*/
void loop() {
    delay(500);
    chosenIndex = readButtons();  

    if (chosenIndex == indexButtonAddTime) {
      addTime();
    } 
    else if (chosenIndex == indexButtonReduceTime) {
      reduceTime();
    }
    else if (chosenIndex == indexButtonStartDown) {
      startCountdownDown();
    }
    else if (chosenIndex == indexButtonStartUp) {
      startCountdownUp();
    }

    displayScore(0);

    Serial.println(counterTime);

  // wait for button input
  // if start button pressed, start counting
  // for 3s intervals, change display from clock to heartrate

}

void addTime() {
  counterTime += 15;
}

void reduceTime() {
  counterTime -= 15;
  
  if (counterTime < 0) {
    counterTime = 0;
  }
}

void startCountdownDown() {
  while (counterTime > 0) {
    displayScore(counterTime--);
    delay(1000);
  }
}

void startCountdownUp() {
  int countHelper = 0;
  
  while (countHelper++ < counterTime) {
    displayScore(countHelper);
    delay(1000);
  }

  counterTime = 0;
}
