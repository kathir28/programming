from chaos_game import ChaosGame


def test_innit_n_value():
    """
    Tests that a ValueError is raised when n,
    the number of corners in the n-gon, is less than 3
    """
    n_gon = ChaosGame(2, 1/2)

def test_innit_n_type():
    """
    Tests that a ValueError is raised when n is a string
    """
    n_gon = ChaosGame('2', 1/2)

def test_init_r_value():
    """
    Tests that a ValueError is raised when r,
    the ratio between the two points, is less than 0 of greater than 1
    """
    n_gon = ChaosGame(4,-0.5)

def test_init_r_type():
    """
    Tests that a ValueError is raised when r is a string
    """
    n_gon = ChaosGame(4,'-0.5')


def test_filetype():
    """
    Tests that a TypeError is raised when a filetype is not .png
    """
    n3 = ChaosGame(3, 1/2)
    n3.iterate(10000)
    n3.savepng("chaos1.jpg")



if __name__ == "__main__":
    #test_innit_n_value()
    #test_innit_n_type()
    #test_init_r_type()
    #test_init_r_value()
    #test_filetype()​