#include <Adafruit_ADS1115.h>
#include <Wire.h>

Adafruit_ADS1115 ads(0x49); //address 0x49 connects VDD to ADDR

//float gainFactor = 0.03125; //dependent on the gain
float voltage;

void setup(void) {
  Serial.begin();
  ads.setGain(GAIN_TWOTHIRDS);
  ads.begin();
}

void loop(void) 
{
  //int16_t adc0;  
  //int16_t adc1;
  //int16_t adc2;
  unsigned long adc0;
  unsigned long adc1;
  unsigned long adc2;
  adc0 = ads.readADC_SingleEnded(0);
  adc1 = ads.readADC_SingleEnded(1);
  adc2 = ads.readADC_SingleEnded(2);
  
  //byte * b1 = (byte *) &adc0;
  //byte * b2 = (byte *) &adc1;
  //byte * b3 = (byte *) &adc2;
  //voltage = (adc0 * gainFactor)/1000;
  //Serial.print("Value: ");
  //Serial.print(adc0);
  //Serial.print("\tVoltage: ");
  Serial.print(adc0); Serial.print(" ");
  //Serial.println();
  Serial.print(adc1); Serial.print(" ");
  //Serial.println();
  Serial.print(adc2); //Serial.print(" ");
  //Serial.print(0);Serial.print(" ");
  Serial.println();
  //Serial.write(b1,2);Serial.write(b2,2);Serial.write(b3,2);
  delay(10);
}
