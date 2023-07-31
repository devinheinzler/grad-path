def calculate_average_rating(ratings):
    """Calculate the average rating from a list of ratings."""
    if not ratings:
        return 0

    total_ratings = sum(ratings)
    average_rating = total_ratings / len(ratings)
    return round(average_rating, 2)