#define A0 36
#define refV 3300 
#define bits 4096.0

float temperature = 0;
int val  = 0;
float temp_celcius = 0;

void setup() {
  Serial.begin(115200);

}

void loop() {
 val  = analogRead(A0);
  temp_celcius = val*(refV/bits);

  temperature = temp_celcius/10.0 ;
  
  Serial.println(temperature);
}
