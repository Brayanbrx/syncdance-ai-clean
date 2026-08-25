import 'package:flutter/material.dart';

class RecordPerformanceScreen extends StatelessWidget {
  const RecordPerformanceScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Grabar performance')),
      body: const Center(
        child: Text('Grabación de performance disponible próximamente'),
      ),
    );
  }
}
