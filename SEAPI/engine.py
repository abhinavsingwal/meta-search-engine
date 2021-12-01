import bing
import gse

googledata=gse.get_gse("abhinav singwal")

print(googledata)
print(type(googledata))
bingdata=(bing.bingsearch("abhinav singwal"))
print(type(bingdata))
print(bingdata)
