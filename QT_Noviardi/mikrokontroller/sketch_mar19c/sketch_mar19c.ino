#define led 3
void setup() {
  // put your setup code here, to run once:
  pinMode(led, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  for(int x=0; x<255; x++){
    analogWrite(led, x);
    delay(5);
  }

  for(int x=255; x>0; x--){
    analogWrite(led, x);
    delay(5);
  }

}
