import lxml
from lxml import etree
youtube = etree.HTML(urllib.urlopen("https://www.youtube.com/watch?v=1ejTKov_Sm4").read()) //enter your youtube url here
video_title = youtube.xpath("//span[@id='eow-title']/@title") //get xpath using firepath firefox addon
print ''.join(video_title)