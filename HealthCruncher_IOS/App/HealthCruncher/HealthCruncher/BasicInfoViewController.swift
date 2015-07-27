//
//  BasicInfoViewController.swift
//  HealthCruncher
//
//  Created by Shaun Mataire on 7/26/15.
//  Copyright (c) 2015 HealthCruncher. All rights reserved.
//

import UIKit

class BasicInfoViewController: UIViewController {
    //text fields
    @IBOutlet weak var zipCode: UITextField!
    @IBOutlet weak var name: UITextField!
    @IBOutlet weak var age: UITextField!
    @IBOutlet weak var weight: UITextField!
    @IBOutlet weak var height: UITextField!
    
    //UISegments
    @IBOutlet weak var sex: UISegmentedControl!
    @IBOutlet weak var race: UISegmentedControl!

    
    override func viewDidLoad() {
        super.viewDidLoad()

        // Do any additional setup after loading the view.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepareForSegue(segue: UIStoryboardSegue, sender: AnyObject?) {
        // Get the new view controller using segue.destinationViewController.
        // Pass the selected object to the new view controller.
        
       //Set input values
        /*
        zipCodeText = zipCode.text
        nameText = name.text
        ageText = age.text
        weightText = weight.text
        heightText = height.text
        sexText = sex.state.rawValue.description
        raceText = race.state.rawValue.description
*/
    }

}
