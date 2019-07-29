# Add your imports here; numpy is only used as an example
import numpy as np


class {{ cookiecutter.container_type.capitalize() }}(object):
    def run(self):
        """This is boilerplate. Delete the contents of this method and put your
        own algorithm code here. Please do not change the class name
        ({{ cookiecutter.container_type.capitalize() }}) or the method name (run).
        """

        with open("/input/example_input_data.txt", "r") as fpin, \
             open("/output/example_output_data.txt", "w") as fpout:
            for l in fpin.readlines():
                try:
                    x, y = [float(i) for i in l.strip().split()]
                except ValueError:
                    continue
                fpout.write("{} {} {}\n".format(x, y**2, x*np.pi))


# Please do not change anything below
if __name__ == "__main__":
    {{ cookiecutter.container_type.capitalize() }}().run()
