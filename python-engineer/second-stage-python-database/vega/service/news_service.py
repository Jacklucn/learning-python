# coding:utf-8

from db.news_dao import NewsDao


class NewsService:
    __news_dao = NewsDao()

    def search_unapproved_list(self, page):
        result = self.__news_dao.search_unapproved_list(page=page)
        return result

    def search_unapproved_count_page(self):
        count_page = self.__news_dao.search_unapproved_count_page()
        return count_page

    def update_unapproved_news(self, news_id):
        self.__news_dao.update_unapproved_news(news_id=news_id)

    def search_list(self, page):
        result = self.__news_dao.search_list(page=page)
        return result

    def search_count_page(self):
        total_page = self.__news_dao.search_count_page()
        return total_page

    def delete_news(self, news_id):
        self.__news_dao.delete_news(news_id=news_id)
