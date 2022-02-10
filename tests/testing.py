import unittest
from app.models import User, Pitches,Upvotes,Downvotes,Comments


class UserModelTest(unittest.TestCase):
  def setUp(self):
    self.new_user=User(usernane="Mishael",email='ratemomishael@gmail.com', pass_secure='mimi')

  def tearDown(self):
    User.query.delete()
    

  def test_password_setter(self):
    self.assertTrue(self.new_user.password_secure is not None)
    
  def test_verify_password(self):
    self.assertTrue(self.new_user.verify_password('mimi'))

  
  def test_unauthorized_access(self):
    with self.assertRaises(AttributeError):
      self.new_user.pass_secure

  
  def test_save_user(self):
    self.new_user.save_user()
    self.assertTrue(len(User.query.all())==1)


class VotesModelTest(unittest.TestCase):
  def setUp(self):
    self.new_user=User(username="Mishael",pass_secure='mimi',role=User.query.filter_by(username='User').first())
    self.new_pitch=Pitches(category=Category.query.filter_by(name='interview').first(),user=self.new_user)
    self.new_vote=Vote(user=self.new_user,pitch=self.new_pitch,upvote=True)

  def tearDown(self):
    Upvotes.query.delete()
    Downvotes.query.delete()    
    Pitches.query.delete()
    User.query.delete()

  def test_instance_variables(self):
    self.assertEquals(self.new_vote.user,self.new_user)
    self.assertEquals(self.new_vote.pitch,self.new_pitch)
    self.assertEquals(self.new_vote.upvote,True)

  def test_save_vote(self):
    self.new_vote.save_vote()
    self.assertTrue(len(Upvotes.query.all())==1)
    self.assertTrue(len(Downvotes.query.all())==1)
    

class PitchesModelTest(unittest.TestCase):
  def setUp(self):
    self.new_user=User(name="Francis",pass_secure='mimi',role=Role.query.filter_by(name='User').first())
    self.new_pitch=Pitches(category=Category.query.filter_by(name='interview').first(),user=self.new_user)

  def tearDown(self):
    Pitches.query.delete()
    User.query.delete()
    

  def test_check_instance_variables(self):

    self.assertEquals(self.new_pitch.user,self.new_user)
    self.assertEquals(self.new_pitch.category,Category.query.filter_by(name='interview').first())

  def test_save_pitch(self):
    self.new_user.save_user()
    self.new_pitch.save_pitch()
    self.assertTrue(len(Pitches.query.all())==1)

class CommentModelTest(unittest.TestCase):
  def setUp(self):
    self.new_user=User(name="Francis",password='password',role=Role.query.filter_by(name='User').first())
    self.new_pitch=Pitches(category=Category.query.filter_by(name='interview').first(),user=self.new_user)
    self.new_comment=Comments(user=self.new_user,pitch=self.new_pitch,content='Good stuff')


  def tearDown(self):
    Comments.query.delete()
    Pitches.query.delete()
    User.query.delete()

  def test_check_instance_variables(self):
    self.assertEquals(self.new_comment.user,self.new_user)
    self.assertEquals(self.new_comment.pitch,self.new_pitch)
    self.assertEquals(self.new_comment.content,'Good stuff')

  def test_save_comment(self):
    self.new_comment.save_comment()
    self.assertTrue(len(Comments.query.all())==1)