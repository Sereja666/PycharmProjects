from passporteye.mrz.image import MRZPipeline
# Import PassportEye
from passporteye import read_mrz


filename = 'C:\PyTest\passport.jpg'
p = MRZPipeline(filename)
mrz = p.result

print(mrz)

# Process image
mrz = read_mrz(filename)

# Obtain image
# mrz_data = mrz.to_dict()
print(mrz)
# print(mrz_data['country'])
# print(mrz_data['names'])
# print(mrz_data['surname'])
# print(mrz_data['type'])
# And so on with the rest of shown properties in the previous JSON string