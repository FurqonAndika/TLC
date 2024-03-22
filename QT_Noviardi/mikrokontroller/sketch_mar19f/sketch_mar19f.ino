#define button 3
#define led 4
int nilai;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(button, INPUT);
  pinMode(led, OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
 nilai = digitalRead(button);

 if(nilai == 1){
  digitalWrite(led, HIGH);
 }

 else{
  digitalWrite(led, LOW);
 }

}
