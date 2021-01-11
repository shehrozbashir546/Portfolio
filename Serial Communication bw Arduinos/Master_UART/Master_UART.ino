//Master Sender
int ButtonValue = 0;
char mystr[15] = "Button Pressed ";
int Button = 3;
char given[10];
int confirm = 1;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(Button, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  ButtonValue= digitalRead(Button);
  if(ButtonValue !=0){
    Serial.write(mystr,15);
    delay(1000);
    // trying to receive a thank you and printing in 
    Serial.readBytes(given,10);
    Serial.println(given);
    delay(1000);
  }
  
  }
