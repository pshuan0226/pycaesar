# pycaesar
A self-attempt of writing a caesar cipher decoder/encoder in python

(pycaesar supports decode with unknown shift)

## Command Line Format
```
usage: pycaesar.py [-h] [-s SHIFT] [-e] [-d] text

pycaesar: ceasar cipher in python

positional arguments:
  text                  text you would like to decode/encode

optional arguments:
  -h, --help            show this help message and exit
  -s SHIFT, --shift SHIFT
                        number of shifts (don't specify if unknown)
  -e, --encode          encodes with ceasar cipher
  -d, --decode          decodes the cipher
```
