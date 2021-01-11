//Slave C6 Reciever
char mystr[15];
char give[10] = "thank you ";
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.readBytes(mystr,15);
  Serial.println(mystr);
  delay(1000);
  //getting a confirmation and
  //sending a thank you back to the master
  if(mystr[0]=='B'){
    Serial.write(give,10);
    delay(1000);
  }
  
  
  
}
