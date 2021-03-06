# EYRA Tools

[![Build Status](https://travis-ci.org/EYRA-Benchmark/eyra-tools.svg?branch=master)](https://travis-ci.org/EYRA-Benchmark/eyra-tools)
[![Documentation Status](https://readthedocs.org/projects/eyra-tools/badge/?version=latest)](https://eyra-tools.readthedocs.io/en/latest/?badge=latest)

EYRA Tools is a Python package that helps you generate Docker containers which
contain a submission or evaluation algorithm for the
[EYRA Benchmark platform](https://www.eyrabenchmark.net).

Benchmark participants should implement their algorithm in a submission
container, while benchmark organizers should implement an evaluation container
to evaluate the output generated by algorithms. The Docker containers
for submissions and evaluations are very similar and can be generated by typing:

```
eyra-generate [submission|evaluation] <container_name> [-d <docker hub account>]
```

For more details on how to use this package, have a look at the
[documentation](https://eyra-tools.readthedocs.io/).

## License

Copyright (c) 2019, Netherlands eScience Center

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
