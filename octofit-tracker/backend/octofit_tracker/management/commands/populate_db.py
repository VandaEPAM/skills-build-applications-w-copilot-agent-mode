from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='dc', description='DC superheroes')

        # Users
        users = [
            User.objects.create(email='tony@stark.com', name='Tony Stark', team='marvel'),
            User.objects.create(email='steve@rogers.com', name='Steve Rogers', team='marvel'),
            User.objects.create(email='bruce@wayne.com', name='Bruce Wayne', team='dc'),
            User.objects.create(email='clark@kent.com', name='Clark Kent', team='dc'),
        ]

        # Activities
        Activity.objects.create(user='tony@stark.com', activity_type='run', duration=30, date='2023-01-01')
        Activity.objects.create(user='steve@rogers.com', activity_type='cycle', duration=45, date='2023-01-02')
        Activity.objects.create(user='bruce@wayne.com', activity_type='swim', duration=60, date='2023-01-03')
        Activity.objects.create(user='clark@kent.com', activity_type='run', duration=50, date='2023-01-04')

        # Leaderboard
        Leaderboard.objects.create(user='tony@stark.com', points=120, rank=1)
        Leaderboard.objects.create(user='steve@rogers.com', points=110, rank=2)
        Leaderboard.objects.create(user='bruce@wayne.com', points=100, rank=3)
        Leaderboard.objects.create(user='clark@kent.com', points=90, rank=4)

        # Workouts
        Workout.objects.create(name='Pushups', description='Do pushups', difficulty='easy')
        Workout.objects.create(name='Situps', description='Do situps', difficulty='easy')
        Workout.objects.create(name='Squats', description='Do squats', difficulty='medium')
        Workout.objects.create(name='Pullups', description='Do pullups', difficulty='hard')

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
