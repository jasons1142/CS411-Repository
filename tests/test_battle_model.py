import pytest

from meal_max.models.battle_model import BattleModel
from meal_max.models.kitchen_model import Meal

@pytest.fixture()
def battle_model():
    """ Fixture to provide a new instance of BattleModel for each test."""
    return BattleModel()

@pytest.fixture
def sample_meal1():
    return Meal(1, "Meal 1", "Cuisine 1", 0.99, "easy")

@pytest.fixture
def sample_meal2():
    return Meal(2, "Meal 2", "Cuisine 2", 1.99, "hard")
    
@pytest.fixture
def sample_battle(sample_meal1, sample_meal2):
    return [sample_meal1, sample_meal2):


def test_battle():

def test_clear_combatants(battle_model, sample_meal1, sample_meal2):
    """ Test clearing the combatants """
    battle_model.combatants = [sample_meal1, sample_meal2)
    battle_model.clear_combatants()
    assert len(battle_model.combatants) == 0, "Playlist should be empty after clearing"

def test_clear_combatants(battle_model, caplog):
    """Test clearing combatants when it's empty."""
    battle_model.clear_combatants()
    assert len(battle_model.combatants) == 0, Combatants should be empty after clearing"
    assert "Clearing empty combatans" in caplog.text, "Expected warning message when clearing empty combatants"
