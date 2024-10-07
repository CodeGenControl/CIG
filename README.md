# CodeGenHub

**CodeGenHub** was created to solve a specific challenge faced by the **FST Lisboa** team, enabling the automated generation of all the necessary code to run the team’s control algorithms. The control code is typically developed using Simulink and exported through the Simulink code generator application. This project aims to streamline the integration of this generated code into the ROS2 environment, making it easier and faster to deploy control systems in the field.

## Overview

The project currently supports the generation of code for two types of ROS2 nodes:

1. **Message Reader Node**: 
   - This node is designed to read messages, typically from a CAN bus line, to integrate various sensors and actuators into the control system.
   - It parses incoming data and publishes it to topics that the control nodes subscribe to.
   - Although it currently supports CAN bus communication, future versions will include support for Ethernet, allowing for broader compatibility with different communication protocols.

2. **Control Node with MATLAB-generated Code**:
   - This node encapsulates control algorithms that are generated directly from MATLAB/Simulink.
   - The generated code is wrapped into a ROS2 node, allowing seamless interaction with other nodes and topics.
   - This makes it easier to deploy complex control systems without needing to manually rewrite the MATLAB/Simulink code into C++.

## Getting Started

To use **CodeGenHub**, you'll need to:
- Define the necessary configuration for your nodes using a JSON file.
- Use the provided interface to simplify the JSON creation process, making it easy to specify message types, topics, and other node parameters.
- Run the code generation tool to produce the complete C++ code for your ROS2 nodes.

## Installation

1. Clone this repository:
   \`\`\`bash
   git clone https://github.com/CodeGenHub/your-repo-name.git
   cd your-repo-name
   \`\`\`

2. Ensure you have Python and the necessary dependencies installed:
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

3. Run the code generator with your JSON configuration:
   \`\`\`bash
   python generate_code.py --config path/to/your/config.json
   \`\`\`

4. Compile the generated code in your ROS2 workspace and launch your nodes.

## Roadmap

- **Version 1.0**: Initial release supporting CAN bus message parsing and MATLAB-generated control nodes.
- **Version 1.1**: Add support for Ethernet communication in the message reader node.
- **Future Plans**: Extend compatibility with other control frameworks and improve the interface for configuration file creation.

## Contribution

Contributions are welcome! If you have suggestions, feature requests, or bug reports, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This project was developed entirely by **André Teixeira**, with the aim of supporting **FST Lisboa** in optimizing their control system deployment.
- Special thanks to the **FST Lisboa** team for providing the requirements and testing environment that made this project possible.
