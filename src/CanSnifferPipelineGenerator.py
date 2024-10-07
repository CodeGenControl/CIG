
from jinja2 import Environment, FileSystemLoader
import json

# Define the path to the directory containing the template file
template_dir = '../templates'  # Assuming template file is in the current directory
template_file_hpp = 'CanSniffer_pipeline.hpp.jinja'
template_file_cpp = 'CanSniffer_pipeline.cpp.jinja'
TorqueVectoring = 'TorqueVectoring.hpp.jinja'

# Create a Jinja2 environment with the file loader
env = Environment(loader=FileSystemLoader(template_dir))

# Load the template from the file
template_hpp = env.get_template(template_file_hpp)

template_cpp = env.get_template(template_file_cpp)

template_controller = env.get_template(TorqueVectoring)


# Define the context from your JSON data
context = json.load(open('../Configs/CanSnifferConfig.json'))
# Render the template with the provided context
generated_code_hpp = template_hpp.render(context)
generated_code_cpp = template_cpp.render(context)
generated_controller = template_controller.render(context)


# Output the generated C++ code (or write to a file)
print(generated_code_hpp)
print(generated_code_cpp)
#print(generated_controller)

# Alternatively, to write the generated code to a file:
with open('../generatedCode/generated_CanSniffer_pipeline.hpp', 'w') as output_file:
    output_file.write(generated_code_hpp)

with open('../generatedCode/generated_CanSniffer_pipeline.cpp', 'w') as output_file:
    output_file.write(generated_code_cpp)

with open('../generatedCode/generated_TorqueVectoring.hpp', 'w') as output_file:
    output_file.write(generated_controller)
