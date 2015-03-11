from matplotlib import pyplot as plt
import matplotlib.image as mpimg
import numpy as np

def check_do_plot(func):
  def inner(self, *args, **kwargs):
    if 'save' in args:
      mpimg.imsave('frame{0}.png'.format(self.counter[0]-1), args[0])
    if self.do_plot:
      return func(self, *args, **kwargs)
    else:
      pass
  return inner

class Plotter(object):
  def __init__(self, plot=True, rows=0, cols=0, num_images=0, folder=None):
    self.counter = [1]
    self.do_plot = plot
    self.folder = folder
    if (rows + cols) == 0 and num_images > 0:
      self.rows = np.ceil(np.sqrt(num_images / 2.0))
      self.cols = np.ceil(num_images / self.rows)
    else:
      self.rows = rows
      self.cols = cols

  @check_do_plot
  def plot_one(self, img, save=False, folder='.'):
    p = plt.subplot(self.rows, self.cols, self.counter[0])
    p.axes.get_xaxis().set_visible(False)
    p.axes.get_yaxis().set_visible(False)
    plt.imshow(img)
    self.counter[0] += 1

  @check_do_plot
  def show(self):
    plt.gcf().subplots_adjust(hspace=0.05, wspace=0,
                              left=0, bottom=0, right=1, top=0.98)
    plt.axis('off')
    plt.show()

  @check_do_plot
  def plot_mesh(self, points, tri, color='k'):
    """ plot triangles """
    for tri_indices in tri.simplices:
      t_ext = [tri_indices[0], tri_indices[1], tri_indices[2], tri_indices[0]]
      plt.plot(points[t_ext, 0], points[t_ext, 1], color)
