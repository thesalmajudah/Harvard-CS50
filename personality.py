
def get_result(selections):
    image_map = {
        '1': 'The Dreamer',
        '2': 'The Achiever',
        '3': 'The Thinker'
    }
    descriptions = {
        'The Dreamer': 'You are intuitive, imaginative, and drawn to nature and art.',
        'The Achiever': 'You are ambitious, energetic, and thrive in dynamic settings.',
        'The Thinker': 'You are analytical, introspective, and value abstract thinking.'
    }
    images = {
        'The Dreamer': 'nature.jpg',
        'The Achiever': 'city.jpg',
        'The Thinker': 'abstract.jpg'
    }
    first_choice = selections.split(',')[0] if selections else '1'
    personality = image_map.get(first_choice, 'The Dreamer')
    return personality, descriptions[personality], images[personality]
