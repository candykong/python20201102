import ast
import yaml
# yaml 实现传递变量的方法
from string import Template

class Common:
    def template(self, yamlName, tp: dict):
        with open(yamlName) as f:
            data = Template(f.read()).substitute(**tp)
            return yaml.safe_load(data)