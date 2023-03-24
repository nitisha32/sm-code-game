
Blockly.Blocks['text_display'] = {
  init: function() {
    this.jsonInit({
      "message0": 'show %1',
      "args0": [
        {
          "type": "input_value",
          "name": "TEXT"
        }
      ],
      "previousStatement": null,
      "nextStatement": null,
      "colour": 255,
      "tooltip": "displays text"
    });
  }
};


Blockly.Blocks['move_up'] = {
  init: function() {
    this.jsonInit({
      "message0": 'move up',
      "previousStatement": null,
      "nextStatement": null,
      "colour": 255,
      "tooltip": "Moves up"
    });
  }
};

Blockly.Blocks['move_down'] = {
  init: function() {
    this.jsonInit({
      "message0": 'move down',
      "previousStatement": null,
      "nextStatement": null,
      "colour": 255,
      "tooltip": "Moves down"
    });
  }
};

Blockly.Blocks['move_left'] = {
  init: function() {
    this.jsonInit({
      "message0": 'move left',
      "previousStatement": null,
      "nextStatement": null,
      "colour": 255,
      "tooltip": "Moves left"
    });
  }
};

Blockly.Blocks['move_right'] = {
  init: function() {
    this.jsonInit({
      "message0": 'move right',
      "previousStatement": null,
      "nextStatement": null,
      "colour": 255,
      "tooltip": "Moves right"
    });
  }
};

Blockly.Blocks['collect'] = {
  init: function() {
    this.jsonInit({
      "message0": 'collect',
      "previousStatement": null,
      "nextStatement": null,
      "colour": 300,
      "tooltip": "Moves right"
    });
  }
};

Blockly.defineBlocksWithJsonArray([ 
{
    "type": "controls_repeat_custom",
    "message0": "%{BKY_CONTROLS_REPEAT_TITLE}",
    "args0": [{
      "type": "field_number",
      "name": "TIMES",
      "value": 10,
      "min": 0,
      "precision": 1
    }],
    "message1": "%1",
    "args1": [{
      "type": "input_statement",
      "name": "DO"
    }],
    "previousStatement": null,
    "nextStatement": null,
    "style": "loop_blocks",
    "tooltip": "%{BKY_CONTROLS_REPEAT_TOOLTIP}",
    "helpUrl": "%{BKY_CONTROLS_REPEAT_HELPURL}"
}   
])


