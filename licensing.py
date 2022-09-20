import sys, datetime, os, base64, random

class License:
  def __init__(self, licenseCode, licenseKey, createdDate, expiryDays):
    self.licenseKey = licenseKey
    self.createdDate = createdDate
    self.licenseCode = licenseCode
    self.secretKey = "secrets69"
    self.expiryDays = int(expiryDays)
  def generateLicense(self):
    def encode_license(key, clear):
      enc = []
      for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
      return base64.urlsafe_b64encode("".join(enc).encode()).decode()
    try:
      originKey = self.licenseCode + "".join([random.choice('abcdefghijklmnopqrstupwxyz0123456789$#&!') for i in range(5)])
      Protected = encode_license(self.secretKey, originKey)
      return Protected
    except:
      pass
  def CheckLicense(self):
    def decode_license(key, enc):
      dec = []
      enc = base64.urlsafe_b64decode(enc).decode()
      for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
      return "".join(dec)
    try:
      revealKey = decode_license(self.secretKey, self.licenseKey)
      if self.licenseCode in revealKey:
        return True
      else:
        sys.exit()
    except:
      sys.exit()
  def CheckExpiry(self):
    try:
      Expiry = datetime.datetime.strptime(self.createdDate, "%Y-%m-%d")
      ExpiryDate = Expiry + datetime.timedelta(days=self.expiryDays)
      if datetime.datetime.now() > expire_date:
        os.remove(f'{sys.argv[0]}')
        sys.exit()
      else:
        pass
    except:
      pass

"""
> Offline simple licensing python script
Features:
- generating license and hide the original license by base64 with secret key
- checking license by breaking the protected license to get the original license with secret Key and when it invalid license the script will self close
- CheckExpiry is checking the expiry date of the script and then self destruction when it expired!

Special thank to @soul_kings

Licensing = License("Code of your license", "License Key, generate first then fill here", "created date of license script to be expired", Howmany days will be expired from the created date)

print(Licensing.generateLicense("Softy", "", "2022-09-20", 31)) # it generate license key with month validity of script

if __name__ == "__main__":
  # Step one you need generate the License key and fill up the LICENSE_KEY, so you can use CheckLicense() and CheckExpiry() function.
  Licensing = License("Softy", "LICENSE_KEY", "2022-09-20", 31)
  print('Generated license key: ' + licensing.generateLicense()) # Generating license key with 1 month validity [31 days] start from date 2022-09-20
  Licensing.CheckLicense() # Check for license valid or not
  Licensing.CheckExpiry() # Check expiry date if expired or not and self descruct when expired !

README!
!!!!    Please obfuscate the script when u doing license system on your script, because when u obfuscste it, it will secure ur license program and license system :D     !!!!
"""
