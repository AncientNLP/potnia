from potnia import linear_a_mapper, linear_b_mapper

def test_to_linear_b():
    assert linear_b_mapper("a-ri-to-jo") == "𐀀𐀪𐀵𐀍" # todo check this is correct
    assert linear_b_mapper("a-ri-to-jo a-ri-to-jo") == "𐀀𐀪𐀵𐀍 𐀀𐀪𐀵𐀍" # todo check this is correct
    


# def test_to_linear_a():
#     assert to_linear_a("]ta-pi ]ki[ ]a-ra[ ]a-su-mi-*118[ a-pa-[?][ ]mi-ki-sa-ne['") == "𐀀𐀪𐀵𐀍" 
    