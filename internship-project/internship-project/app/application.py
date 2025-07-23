

from pages.base_page import Page
from pages.sign_in_page import SignInPage
from pages.reelly_project import ReellyProject

class Application:
    def __init__(self, driver):
        self.base_page = Page(driver)
        self.reelly_project = ReellyProject(driver)
        self.sign_in_page = SignInPage(driver)
        #self.header = Header(driver)
        #self.search_results_page = SearchResultsPage(driver)
        #self.cart_page = Cartpage(driver)
        #self.side_navigation_cart = SideNavigationCart(driver)
        #self.target_terms_condns = TargetTermsCondns(driver)
