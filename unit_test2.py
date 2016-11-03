import unittest

from dgame import Dgame

class GameTests(unittest.TestCase):
    
    #Setup method to create test object
    def setUp(self):
        print("Setting up!")
        self.newgame = Dgame("titteli")

    #Teardown method to delete the test object
    def tearDown(self):
        print("Tearing down!")
        del self.newgame
        
    def test_title_is_string(self):
        self.assertTrue(isinstance(self.newgame.get_title(), str), "test failed! title not string!")
  
  
if __name__ == '__main__':
    unittest.main()
