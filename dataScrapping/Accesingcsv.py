import gdata.youtube
import gdata.youtube.service

yt_service = gdata.youtube.service.YouTubeService()

yt_service.ssl = True
yt_service.developer_key = 'AIzaSyAmmVvu2Zl3iu-2k2CTiDuaI5gP7OLrmqc'


# This prints the related video list

related_feed = yt_service.GetYouTubeRelatedVideoFeed(video_id='ocGiulPm3IU')

print(type(related_feed))

entry = yt_service.GetYouTubeVideoEntry(video_id='the0KZLEacs')

related_feed = yt_service.GetYouTubeRelatedVideoFeed(video_id='abc123')

def PrintEntryDetails(entry):
  print('Video title: %s' % entry.media.title.text)
  print('Video published on: %s ' % entry.published.text)
  print('Video description: %s' % entry.media.description.text)
  print('Video category: %s' % entry.media.category[[]].text)
  print('Video tags: %s' % entry.media.keywords.text)
  print('Video watch page: %s' % entry.media.player.url)
  print('Video flash player URL: %s' % entry.GetSwfUrl())
  print('Video duration: %s' % entry.media.duration.seconds)

  # non entry.media attributes
  print('Video geo location: %s' % entry.geo.location())
  print('Video view count: %s' % entry.statistics.view_count)
  print('Video rating: %s' % entry.rating.average)

  # show alternate formats
  for alternate_format in entry.media.content:
    if 'isDefault' not in alternate_format.extension_attributes:
      print('Alternate format: %s | url: %s ' % (alternate_format.type,
                                                 alternate_format.url))

  # show thumbnails
  for thumbnail in entry.media.thumbnail:
    print('Thumbnail url: %s' % thumbnail.url)

def GetAndPrintVideoFeed(uri):
  yt_service = gdata.youtube.service.YouTubeService()
  feed = yt_service.GetYouTubeVideoFeed(uri)
  for entry in feed.entry:
    PrintEntryDetails(entry)


def SearchAndPrintVideosByKeywords(list_of_search_terms):
  yt_service = gdata.youtube.service.YouTubeService()
  query = gdata.youtube.service.YouTubeVideoQuery()
  query.orderby = 'viewCount'
  query.racy = 'include'
  for search_term in list_of_search_terms:
    new_term = search_term.lower()
    query.categories.append('/%s' % new_term)
  feed = yt_service.YouTubeQuery(query)
  PrintVideoFeed(feed)