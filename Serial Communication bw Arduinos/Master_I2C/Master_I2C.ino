#include <Wire.h>
#define SLAVE_ADDR 9
#define ANSWERSIZE 9
char str = 'a';
void setup() {
  // Initialize I2C communications as Master
  Wire.begin();
  // Setup serial monitor
  Serial.begin(9600);
 }
 
void loop() {
  delay(500);
   // Write a character to the Slave
  Wire.beginTransmission(SLAVE_ADDR);
  Wire.write(str);
  Wire.endTransmission();
  // Read response from Slave
  // Read back 5 characters
  Wire.requestFrom(SLAVE_ADDR,ANSWERSIZE);
  
  // Add characters to string
  String response = "";
  while (Wire.available()) {
      char b = Wire.read();
      response += b;
  } 
  
  // Print to Serial Monitor
  Serial.println(response);
}
