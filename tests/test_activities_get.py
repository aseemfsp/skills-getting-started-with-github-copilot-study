def test_get_activities_returns_all_seeded_activities(client):
    # Arrange
    expected_activities = {
        "Chess Club",
        "Programming Class",
        "Gym Class",
        "Basketball Team",
        "Tennis Club",
        "Art Studio",
        "Music Band",
        "Debate Team",
        "Science Club",
    }

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    payload = response.json()
    assert isinstance(payload, dict)
    assert set(payload.keys()) == expected_activities


def test_get_activities_returns_participants_as_lists(client):
    # Arrange
    activity_name = "Chess Club"

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    payload = response.json()
    assert "participants" in payload[activity_name]
    assert isinstance(payload[activity_name]["participants"], list)
    assert "michael@mergington.edu" in payload[activity_name]["participants"]
