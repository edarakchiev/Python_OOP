import unittest
from project.hero import Hero


class HeroTest(unittest.TestCase):

    def setUp(self):
        self.hero = Hero("test_name", 3, 100, 4)

    def test_init_method(self):
        self.assertEqual(self.hero.username, "test_name")
        self.assertEqual(self.hero.level, 3)
        self.assertEqual(self.hero.health, 100)
        self.assertEqual(self.hero.damage, 4)

    def test_battle__when_names_is_identical__expected_exception(self):
        enemy_hero = Hero("test_name", 5, 8, 2)
        with self.assertRaises(Exception) as context:
            self.hero.battle(enemy_hero)
        self.assertEqual(context.exception.args[0], "You cannot fight yourself")

    def test_battle__when_self_health_is_negative_expected_exception(self):
        enemy_hero = Hero("test_name_2", 5, 8, 2)
        self.hero.health = 0
        with self.assertRaises(Exception) as context:
            self.hero.battle(enemy_hero)
        self.assertEqual(context.exception.args[0], "Your health is lower than or equal to 0. You need to rest")

    def test_battle__when_enemy_health_is_negative__expected_exception(self):
        enemy_hero = Hero("test_name_2", 5, 0, 2)
        with self.assertRaises(Exception) as context:
            self.hero.battle(enemy_hero)
        self.assertEqual(context.exception.args[0], f"You cannot fight test_name_2. He needs to rest")

    def test_battle__when_data_is_correct__expected_execute(self):
        enemy_hero = Hero("test_name_2", 5, 8, 2)
        self.hero.battle(enemy_hero)
        self.assertEqual(-4, enemy_hero.health)
        self.assertEqual(95, self.hero.health)
        self.assertEqual(4, self.hero.level)
        self.assertEqual(9, self.hero.damage)

    def test_battle__when_health_is_zero__expected_exception(self):
        test_hero = Hero("test", 5, 8, 2)
        enemy_hero = Hero("test_name_2", 5, 8, 2)
        result = test_hero.battle(enemy_hero)
        self.hero.health = 0
        enemy_hero.health = 0
        self.assertEqual("Draw", result)

    def test_battle__when_hero_health_is_biggest__expected_execute(self):
        enemy_hero = Hero("test_name_2", 5, 8, 2)
        self.assertEqual("You win", self.hero.battle(enemy_hero))

    def test_battle__when_hero_health_is_zero__expected_execute(self):
        enemy_hero = Hero("test_name_2", 50, 150, 2)
        result = self.hero.battle(enemy_hero)
        self.assertEqual(0, self.hero.health)
        self.assertEqual(51, enemy_hero.level)
        self.assertEqual(143, enemy_hero.health)
        self.assertEqual(7, enemy_hero.damage)
        self.assertEqual("You lose", result)

    def test_str_method(self):
        expected = f"Hero test_name: 3 lvl\nHealth: 100\nDamage: 4\n"
        actual = self.hero.__str__()
        self.assertEqual(expected, actual)
