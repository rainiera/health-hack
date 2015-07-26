//
//  MedicalHstoryViewController.swift
//  HealthCruncher
//
//  Created by Shaun Mataire on 7/26/15.
//  Copyright (c) 2015 HealthCruncher. All rights reserved.
//

import UIKit

class MedicalHstoryViewController: UIViewController {

    @IBOutlet weak var LifeTreatSeg: UISegmentedControl!
    @IBOutlet weak var diabeticsSeg: UISegmentedControl!
    @IBOutlet weak var heartDiseaseSeg: UISegmentedControl!
    @IBOutlet weak var otherDiseasesSeg: UISegmentedControl!
    
    override func viewDidLoad() {
        super.viewDidLoad()

        // Do any additional setup after loading the view.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    

    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepareForSegue(segue: UIStoryboardSegue, sender: AnyObject?) {
        // Get the new view controller using segue.destinationViewController.
        // Pass the selected object to the new view controller.
    }
    */

}
