#include <OneWire.h>
#include <DallasTemperature.h>

#define ONE_WIRE_BUS 2;

OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature  temp(&oneWire);

void setup(void) {
  temp.setResolution(12);
  Serial.begin();
  temp.begin();
}

void loop(void) {
  temp.requestTemperatures();
  Serial.print(
  Serial.print(temp.getTempCByIndex(0));
  Serial.print(temp.getTempFByIndex(0));

}
