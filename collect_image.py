from icrawler.builtin import GoogleImageCrawler
import sys
args = sys.argv
crawler = GoogleImageCrawler(storage={"root_dir":args[1]})
crawler.crawl(keyword=args[2],max_num=100)
