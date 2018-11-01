import urllib
import os
import zipfile
from glob import glob

surah = 1 #alfatihah
os.system("rm -rf ../audio/*") #clearing folder audio first
os.system("mkdir -p ../audio/training_set")
os.system("mkdir -p ../audio/test_set")

def download(urls, isTrainingSet):
	i = 1
	folder_t = ""
	rename_surah = "{0:0=3d}".format(surah)

	for url in urls:
		if (isTrainingSet):
			folder_t = "../audio/training_set/"+str(i)
		else:
			folder_t = "../audio/test_set/"+str(i)
		
		os.system("mkdir "+folder_t)
		file_name = folder_t+"/"+rename_surah+".zip"

		print "Downloading: "+url+rename_surah+".zip"
		testfile = urllib.URLopener()
		testfile.retrieve(url+rename_surah+".zip", file_name)

		print "Unzipping..."
		zip_ref = zipfile.ZipFile(file_name, 'r')
		zip_ref.extractall(folder_t)
		zip_ref.close()

		i = i + 1

url_trains =	[
			"http://www.everyayah.com/data/Abdul_Basit_Mujawwad_128kbps/zips/",
		#"http://www.everyayah.com/data/Abdullaah_3awwaad_Al-Juhaynee_128kbps/zips/",
		#"http://www.everyayah.com/data/Abdullah_Basfar_192kbps/zips/",
		#"http://www.everyayah.com/data/Abdullah_Matroud_128kbps/zips/",
		#"http://www.everyayah.com/data/Abdurrahmaan_As-Sudais_192kbps/zips/",
		#"http://www.everyayah.com/data/Abu_Bakr_Ash-Shaatree_128kbps/zips/",
		#"http://www.everyayah.com/data/Ahmed_Neana_128kbps/zips/",
		#"http://www.everyayah.com/data/Ahmed_ibn_Ali_al-Ajamy_128kbps_ketaballah.net/zips/",
		#"http://www.everyayah.com/data/Akram_AlAlaqimy_128kbps/zips/",
		#"http://www.everyayah.com/data/Alafasy_128kbps/zips/",
		#"http://www.everyayah.com/data/Ali_Hajjaj_AlSuesy_128kbps/zips/",
		#"http://www.everyayah.com/data/Ali_Jaber_64kbps/zips/",
		#"http://www.everyayah.com/data/Fares_Abbad_64kbps/zips/",
		#"http://www.everyayah.com/data/Ghamadi_40kbps/zips/",
		#"http://www.everyayah.com/data/Hani_Rifai_192kbps/zips/",
		#"http://www.everyayah.com/data/Hudhaify_128kbps/zips/",
		#"http://www.everyayah.com/data/Husary_128kbps/zips/",
		#"http://www.everyayah.com/data/Husary_Muallim_128kbps/zips/",
		#"http://www.everyayah.com/data/Husary_Mujawwad_64kbps/zips/",
		#"http://www.everyayah.com/data/Ibrahim_Akhdar_32kbps/zips/",
		#"http://www.everyayah.com/data/Karim_Mansoori_40kbps/zips/",
		#"http://www.everyayah.com/data/Khaalid_Abdullaah_al-Qahtaanee_192kbps/zips/",
		#"http://www.everyayah.com/data/MaherAlMuaiqly128kbps/zips/",
		#"http://www.everyayah.com/data/Menshawi_16kbps/zips/",
		#"http://www.everyayah.com/data/Muhammad_AbdulKareem_128kbps/zips/",
		#"http://www.everyayah.com/data/Muhammad_Ayyoub_128kbps/zips/",
		#"http://www.everyayah.com/data/Muhammad_Jibreel_64kbps/zips/",
		#"http://www.everyayah.com/data/Muhsin_Al_Qasim_192kbps/zips/",
		#"http://www.everyayah.com/data/Nasser_Alqatami_128kbps/zips/",
		#"http://www.everyayah.com/data/Sahl_Yassin_128kbps/zips/",
		#"http://www.everyayah.com/data/Salaah_AbdulRahman_Bukhatir_128kbps/zips/",
		#"http://www.everyayah.com/data/Salah_Al_Budair_128kbps/zips/",
		#"http://www.everyayah.com/data/Yaser_Salamah_128kbps/zips/",
		#"http://www.everyayah.com/data/aziz_alili_128kbps/zips/",
		#"http://www.everyayah.com/data/ahmed_ibn_ali_al_ajamy_128kbps/zips/",
		#"http://www.everyayah.com/data/Yasser_Ad-Dussary_128kbps/zips/",
		#"http://www.everyayah.com/data/mahmoud_ali_al_banna_32kbps/zips/",
		#"http://www.everyayah.com/data/khalefa_al_tunaiji_64kbps/zips/",
			]

url_tests = [

	]

download(url_trains, True)
download(url_tests, False)

print "Converting all of the files to wav..."
result = [y for x in os.walk("../audio") for y in glob(os.path.join(x[0], '*.mp3'))]

for r in result:
	print "Processing: ffmpeg -i "+r+" -acodec pcm_u8 -ar 22050 "+r+".wav > /dev/null 2>&1"
	os.system("ffmpeg -i "+r+" -acodec pcm_u8 -ar 22050 "+r+".wav > /dev/null 2>&1")

