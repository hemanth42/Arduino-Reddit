void setup() {
  // open the serial port:
Serial.begin(9600);
  // initialize control over the keyboard:
  pinMode(13, OUTPUT);
  
}

void blinktwice()
{
   digitalWrite(13, LOW);
   digitalWrite(13, HIGH);
   delay(100);
   digitalWrite(13, LOW);
   delay(100);
   digitalWrite(13, HIGH);
   delay(100);
   digitalWrite(13, LOW);
  
}

void loop() {
  // check for incoming serial data:
  if (Serial.available() > 0) {  
    // read incoming serial data:
    char inChar = Serial.read();
    
    if (true) { Serial.println(inChar); }
    
    // Typing 'h' in the serial monitor will turn on LED on pin 13
    // Typing anything else will make it LOW
    
    if(inChar == 'h') { digitalWrite(13, HIGH); }
    else if(inChar == 'b') { blinktwice(); }
    else {
      digitalWrite(13, LOW);
         } 
      
  }  
}

