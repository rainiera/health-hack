//
//  PersonalHealthViewController.swift
//  HealthCruncher
//
//  Created by Shaun Mataire on 7/26/15.
//  Copyright (c) 2015 HealthCruncher. All rights reserved.
//

import UIKit

class PersonalHealthViewController: UIViewController {

    @IBOutlet weak var physicalActSeg: UISegmentedControl!
    @IBOutlet weak var stressSeg: UISegmentedControl!
    @IBOutlet weak var hygieneSeg: UISegmentedControl!
    @IBOutlet weak var diettSeg: UISegmentedControl!
    @IBOutlet weak var emotionalSeg: UISegmentedControl!
    @IBOutlet weak var happinessSeg: UISegmentedControl!
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
