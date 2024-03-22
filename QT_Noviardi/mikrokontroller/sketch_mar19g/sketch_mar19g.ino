#define led 3
#define button 4
unsigned long waktu_awal = 0;
unsigned long waktu_sekarang = 0;
bool led_state = false;

void setup() {
  // put your setup code here, to run once:
  pinMode(button, INPUT_PULLUP);
  pinMode(led, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.println(!digitalRead(button));
  waktu_awal = millis();
  if (waktu_awal-waktu_sekarang>1000){
    waktu_sekarang = waktu_awal;
    led_state = !led_state;
    digitalWrite(led, led_state);
  }

}
