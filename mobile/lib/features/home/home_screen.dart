import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';

class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Inicio')),
      body: ListView(
        padding: const EdgeInsets.all(16),
        children: [
          ListTile(
            title: const Text('Rutinas'),
            trailing: const Icon(Icons.chevron_right),
            onTap: () => context.push('/routines'),
          ),
          ListTile(
            title: const Text('Performances'),
            trailing: const Icon(Icons.chevron_right),
            onTap: () => context.push('/performances'),
          ),
        ],
      ),
    );
  }
}
