#!/bin/sh
interrupt() {
    echo ''
    echo 'interrupt'
}
trap 'interrupt' 2
echo "Generally, any device that can perform numerical calculations, even an adding machine, may be called a computer but nowadays this term is used especially for digital computers. Computers that once weighed 30 tons now may weigh as little as 1.8 kilograms. Microchips and microprocessors have considerably reduced the cost of the electronic components required in a computer. Computers come in many sizes and shapes such as special-purpose, laptop, desktop, minicomputers, supercomputers. Special-purpose computers can perform specific tasks and their operations are limited to the programmes built into their microchips. There computers are the basis for electronic calculators and can be found in thousands of electronic products, including digital watches and automobiles. Basically, these computers do the ordinary arithmetic operations such as addition, subtraction, multiplication and division. General-purpose computers are much more powerful because they can accept new sets of instructions. T" > ab.txt

sleep 1
sleep 1
sleep 1

#cat ab.txt| awk '{for(i=1;i<=length;i++) print i,substr($0,i,1);}'|tr '\n' ' '|cat > ab.txt
cat ab.txt| awk '{split($0,chars,"");f="";for(i=1;i<=length($0); i++) f=f i chars[i]; print f}'| sed 's/[0-9][0-9]*/& /g'|tee ab.txt

while :
do
  echo 'Enter "q" to stop'
  read command
  if [ "$command" = "q" ];
  then
    exit 0
  fi
done
