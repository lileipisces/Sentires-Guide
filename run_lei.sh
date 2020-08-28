python lei/0.format.py

java -jar thuir-sentires.jar -t pre -c lei/1.pre

java -jar thuir-sentires.jar -t pos -c lei/2.pos

cp lei/intermediate/pos.1.txt lei/intermediate/pos.2.txt

java -jar thuir-sentires.jar -t validate -c lei/3.validate

java -jar thuir-sentires.jar -t lexicon -c lei/4.lexicon.linux

java -jar thuir-sentires.jar -t profile -c lei/5.profile

python lei/6.transform.py

python lei/7.match.py