def data_create_segment(segment_name):
    return {
        'name': f'{segment_name}',
        'pass_condition': 1,
        'logicType': 'or',
        "relations": [{"object_type": "remarketing_player",
                       "params": {"type": "positive", "left": 365, "right": 0}}],
    }


def data_create_campaign(name, primary_id, id):
    return {
        "name": name,
        "read_only": False,
        "conversion_funnel_id": None,
        "objective": "reach",
        "targetings": {"split_audience": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "sex": ["male", "female"],
                       "age": {
                           "age_list": [0, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
                                        30, 31, 32, 33,
                                        34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52,
                                        53, 54, 55,
                                        56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74,
                                        75]}},
        "autobidding_mode": "max_shows",
        "uniq_shows_period": "day",
        "budget_limit_day": "100",
        "budget_limit": "100",
        "mixing": "recommended",
        "enable_utm": True,
        "price": "21",
        "max_price": "0",
        "package_id": 960,
        "banners": [
            {"urls": {"primary": {"id": f'{primary_id}'}}, "textblocks": {},
             "content": {"image_240x400": {"id": f'{id}'}},
             "name": ""}]
    }
