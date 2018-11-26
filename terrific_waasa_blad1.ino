int dioda = 13;
int czas;
void setup(){
    pinMode(dioda, OUTPUT);
}
void loop(){
    for (int i = 0; i < 9; i = i + 1){
      if (i<3 || i>=6) {
        czas=500;
      }
      else {
        czas=1500;
      }
     
        digitalWrite(dioda, HIGH); 
        delay(czas);
        digitalWrite(dioda, LOW); 
        delay(czas);
    }
 
    delay(3000);
};